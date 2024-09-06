import { useState } from "react";
import styled from "styled-components";
 
const Wrapper = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 420px;
  padding: 50px 0px;
`;

const Title = styled.h1`
  font-size: 42px;
`;

const Form = styled.form`
  margin-top: 50px;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
`;

const Input = styled.input`
  padding: 10px 20px;
  border-radius: 50px;
  border: none;
  width: 100%;
  font-size: 16px; 
  &[type="submit"] {
    cursor: pointer;
    &:hover {
      opacity: 0.8;
    }
  }
`;
 
const Error = styled.span`
  font-weight: 600;
  color: tomato;

`
export default function CreateAccount() {
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
    
    const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      console.log(name, email, password); 

      try {
        // do somthing
      } catch(e) {
        // do somthing when raised error
      } finally {
        setLoading(false);
      } 
    }

    return (
        <Wrapper>
          <Title> Log into 🙅‍♂️</Title>
            <Form onSubmit={onSubmit}>
                <Input name="name" value={name} placeholder="Name" type="text" onChange={onChange} required />
                <Input name="email" value={email} placeholder="Email" type="email" onChange={onChange} required />
                <Input name="password" value={password}  placeholder="Password" type="password" onChange={onChange} required />
                <Input name="submit" value={isLoading ? "Loading..." :  "Create Account"} type="submit" /> 
            </Form>
            {error !== "" ? <Error>{erorr}</Error> : null}
        </Wrapper>
    );
}
