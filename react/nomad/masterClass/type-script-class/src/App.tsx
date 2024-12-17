import styled from "styled-components";
import { motion, Variants } from "motion/react";
import { useRef } from "react";

const Wrapper = styled.div`
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const BiggerBox = styled(motion.div)`
  width: 600px;
  height: 600px;
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  /* overflow: hidden; */
`;

const Box = styled(motion.div)`
  width: 200px;
  height: 200px;
  background-color: rgba(255, 255, 255, 1);
  border-radius: 40px;
  box-shadow: 0 2px 3px rg ba(0, 0, 0, 0.1), 0 10px 20px rgba(0, 0, 0, 0.06);
`;

const boxVariants: Variants = {
  hover: { scale: 1.5, rotateZ: 90 },
  click: { scale: 1, borderRadius: "100px" },
  drag: {
    backgroundColor: "rgb(46, 204, 113)",
    transition: {
      duration: 10,
    },
  },
};

function App() {
  const biggerBoxRef = useRef<HTMLDivElement>(null);

  // If u use right props, u can do anything !
  return (
    <Wrapper>
      <BiggerBox ref={biggerBoxRef}>
        <Box
          drag // we can fix its axis by setting darg="x" or "y"
          dragSnapToOrigin
          dragElastic={0.5}
          dragConstraints={biggerBoxRef}
          variants={boxVariants}
          whileHover="hover"
          whileTap="click"
          whileDrag="drag" // It should be rgb, if u not use color string
        />
      </BiggerBox>
    </Wrapper>
  );
}

export default App;
