import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { FirebaseError } from "firebase/app";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../src/firebase";
import { Form, Error, Input, Switcher, Title, Wrapper } from '../components/auth-components';
import GithubButton from '../components/github-btn';


export default function Login() {
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const name = e.target.name;
        const value = e.target.value;

        switch (name) {
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

      if (isLoading || email === "" || password === "") return;

      try {
        setLoading(true);
        await signInWithEmailAndPassword(auth, email, password);
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
          <Title> Log into  🙅‍♂️ </Title>
          <Form onSubmit={onSubmit}>
            <Input name="email" value={email} placeholder="Email" type="email" onChange={onChange} required />
            <Input name="password" value={password}  placeholder="Password" type="password" onChange={onChange} required />
            <Input name="submit" value={isLoading ? "Loading..." :  "Log In"} type="submit" /> 
          </Form>
          <Switcher>Don't have an account ? {" "}
            <Link to="/create-account">Create an account &rarr;</Link>
          </Switcher>
          <GithubButton />
          {error !== "" ? <Error>{error}</Error> : null}
        </Wrapper>
    );
}
