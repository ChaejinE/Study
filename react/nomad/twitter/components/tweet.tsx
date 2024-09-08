import styled from "styled-components";
import { ITweet } from "./timeline";
import { auth, db, storage } from "../src/firebase";
import { deleteDoc, doc, updateDoc } from "firebase/firestore";
import { deleteObject, getDownloadURL, ref, uploadBytes } from "firebase/storage";
import { useState } from "react";

const Wrapper = styled.div`
  display: grid;
  grid-template-columns: 3fr 1fr;
  padding: 20px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 15px;
`;

const Column = styled.div``;

const Photo = styled.img`
  width: 100px;
  height: 100px;
  border-radius: 15px;
`;

const Username = styled.span`
  font-weight: 600;
  font-size: 15px;
`;

const Payload = styled.p`
  margin: 10px 0px;
  font-size: 18px;
`;

const TextArea = styled.textarea`
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

const DeleteButton = styled.button`
  background-color: tomato;
  color: white;
  font-weight: 600;
  border: 0;
  font-size: 12px;
  padding: 5px 10px;
  text-transform: uppercase;
  border-radius: 5px;
  cursor: pointer;
`;

const EditButton = styled.button`
  background-color: skyblue;
  margin: 5px 5px;
  color: white;
  font-weight: 600;
  border: 0;
  font-size: 12px;
  padding: 5px 10px;
  text-transform: uppercase;
  border-radius: 5px;
  cursor: pointer;
`;

const AttachFileButton = styled.label`
  background-color: skyblue;
  color: white;
  font-weight: 600;
  border: 0;
  font-size: 12px;
  padding: 5px 10px;
  text-transform: uppercase;
  border-radius: 5px;
  cursor: pointer;
`;

const AttachFileInput = styled.input`
  display: none;
`;


export default function Tweet({userId, username, photo, tweet, id}: ITweet) {
  const [isEdit, setEdit] = useState(false);
  const [tweet_, setTweet] = useState(tweet);
  const [file, setFile] = useState<File | null>(null);
  const user = auth.currentUser;

  const onDelete = async () => {
    const ok = confirm("Are you sure you wanna delete this tweet ? ");

    if (!ok || user?.uid !== userId) return;

    try {
      await deleteDoc(doc(db, "tweets", id));
      if (photo) {
        const photoRef = ref(storage, `tweets/${user.uid}/${id}`);
        await deleteObject(photoRef);
      }
    } catch (e) {
      console.error(e);
    }
  }

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

  const onEdit = async () => {
    if (!isEdit) {
      setEdit(true);
      return;
    }

    if (user?.uid !== userId) return;

    try {
      if (file) {
        const locationRef = ref(storage, `tweets/${user.uid}/${id}`);
        const result = await uploadBytes(locationRef, file);
        photo = await getDownloadURL(result.ref);
      }

      const docRef = doc(db, "tweets", id);
      
      await updateDoc(docRef, {
        tweet: tweet_,
        photo: photo || null,
        createdAt: Date.now()
      });
    } catch (e) {
      console.error(e);
    } finally {
      if (isEdit) {
        setEdit(false);
        setFile(null);
      }
    }
  }
  
  return(
    <Wrapper>
      <Column>
        <Username>{username}</Username>
        {isEdit ?
          <TextArea onChange={onChange} value={tweet_}></TextArea> 
          : 
          <Payload>{tweet_}</Payload>
        }
        {user?.uid === userId ? <DeleteButton onClick={onDelete}>Delete</DeleteButton> : null}
        {user?.uid === userId ? <EditButton onClick={onEdit}>{isEdit ? "Save" : "Edit" }</EditButton> : null}
        {isEdit ? <AttachFileButton htmlFor="file-edit">{file ? "Photo added 📌" : "Add photo"}</AttachFileButton> : null}
        {isEdit ? <AttachFileInput onChange={onFileChange} id="file-edit" type="file" accept="image/*" /> : null}
      </Column>
      <Column>
        { photo ? <Photo src={photo} /> : null }
      </Column> 
    </Wrapper>
  );
}
