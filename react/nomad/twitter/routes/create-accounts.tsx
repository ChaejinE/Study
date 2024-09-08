import { createUserWithEmailAndPassword, updateProfile } from "firebase/auth";
import { useState } from "react";
import { auth } from "../src/firebase";
import { Link, useNavigate } from "react-router-dom";
import { FirebaseError } from "firebase/app";
import { Form, Error, Input, Switcher, Title, Wrapper } from "../components/auth-components";
import GithubButton from "../components/github-btn";

export default function CreateAccount() {
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const name = e.target.name;
        const value = e.target.value;

        switch (name) {
          case 'name': 
            setName(value);
            break;
          case 'email':
            setEmail(value);
            break;
          case 'password':
            setPassword(value);
            break;
        }
    }
    
    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      console.log(name, email, password); 

      if (isLoading || name === "" || email === "" || password === "") return;

      try {
        setError("");
        setLoading(true);
        const credentials = await createUserWithEmailAndPassword(auth, email, password);
        console.log(credentials.user);
        await updateProfile(credentials.user, {
          displayName: name,
        })
        navigate("/");
      } catch(e) {
        if (e instanceof FirebaseError) {
          setError(e.message);
        }
      } finally {
        setLoading(false);
      } 
    }

    return (
        <Wrapper>
          <Title> Join 🙅‍♂️</Title>
          <Form onSubmit={onSubmit}>
            <Input name="name" value={name} placeholder="Name" type="text" onChange={onChange} required />
            <Input name="email" value={email} placeholder="Email" type="email" onChange={onChange} required />
            <Input name="password" value={password}  placeholder="Password" type="password" onChange={onChange} required />
            <Input name="submit" value={isLoading ? "Loading..." :  "Create Account"} type="submit" /> 
          </Form>
          <Switcher>Already have an account ? {"  "}
            <Link to="/login">Log In &rarr;</Link>
          </Switcher>
          <GithubButton />
          {error !== "" ? <Error >{error}</Error> : null}
        </Wrapper>
    );
}
