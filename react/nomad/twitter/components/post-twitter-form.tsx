import React, { useState } from "react";
import styled from "styled-components"
import { auth, db, storage } from "../src/firebase";
import { addDoc, collection, updateDoc } from "firebase/firestore";
import { getDownloadURL, ref, uploadBytes } from "firebase/storage";

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 10px;
`;

export const TextArea = styled.textarea`
  border: 2px solid white;
  padding: 20px;
  border-radius: 20px;
  font-size: 16px;
  color: white;
  background-color: black;
  width: 100%;
  resize: none;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  &::placeholder {
    font-size: 16px;
  }
  &:focus {
    outline: none;
    border-color: #1d9bf0;
  }
`;

const AttachFileButton = styled.label`
  padding: 10px 0px;
  color: #1d9df0;
  text-align: center;
  border-radius: 20px;
  border: 1px solid #1d9df0;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
`;

const AttachFileInput = styled.input`
  display: none;
`;

const SubmitBtn = styled.input`
  background-color: #1d9bf0;
  color: white;
  border: none;
  padding: 10px 0px;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  &:hover,
  &:active {
    opacity: 0.9;
  }
`;

export default function PostTweetForm() {
  const [isLoading, setLoading] = useState(false);
  const [tweet, setTweet] = useState("");
  const [file, setFile] = useState<File | null>(null);

  const maxTweetLength = 180;
  
  const onChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setTweet(e.target.value);
  }

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { files } = e?.target;
    const oneKB = 1024;
    const maxFileSize = oneKB * 1000000;

    if (files || files.length === 1) { // We wanna a file so that we just check only one
      const file = files[0];
      if (file.size > maxFileSize) {
        alert("Excceded file size")
      } else {
        setFile(file);
      }
    }
  }

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const user = auth.currentUser;

    if (!user || isLoading || tweet === "" || tweet.length > maxTweetLength) return;

    try {
      setLoading(true);
      const doc = await addDoc(collection(db, "tweets"), {
        tweet,
        createdAt: Date.now(),
        username: user.displayName || "Anonymous", 
        userId: user.uid,
        photo: null
      })

      if (file) {
        const locationRef = ref(storage, `tweets/${user.uid}/${doc.id}`);
        const result = await uploadBytes(locationRef, file);
        const url = await getDownloadURL(result.ref);
        await updateDoc(doc, {
          photo: url
        });
      }
      setTweet("");
      setFile(null);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Form onSubmit={onSubmit}>
      <TextArea rows={5} maxLength={maxTweetLength} onChange={onChange} value={tweet} placeholder="What is happening ?" required/> 
      <AttachFileButton htmlFor="file">{file ? "Photo added 📌" : "Add photo"}</AttachFileButton>
      <AttachFileInput onChange={onFileChange} id="file" type="file" accept="image/*" />
      <SubmitBtn type="submit" value={isLoading ? "Posting..." : "Post Tweet"} />
    </Form>
  );
}
