import { useState } from "react";
import styled from "styled-components"

interface ContainerProps {
  bgColor: string
  borderColor : string;
}

const Container = styled.div<ContainerProps>`
  width: 200px;
  height: 200px;
  background-color: ${props => props.bgColor};
  border-radius: 100px;
  border: 1px solid ${props => props.borderColor};
`;

// describe the props of Circle
interface CircleProps {
  bgColor: string
  borderColor?: string
}

function Circle({ bgColor, borderColor} : CircleProps) {
    const [value, setValue] = useState<number | string>(1);
    setValue(2);
    setValue("hello"); // no error

    return ( 
      <Container bgColor={bgColor} borderColor={borderColor ?? bgColor} />
    );
}

export default Circle;
