import PostTweetForm from '../components/post-twitter-form';
import TimeLine from "../components/timeline";
import styled from "styled-components";

const Wrapper = styled.div`
  display: grid;
  gap: 50px;
  overflow-y: scroll;
  grid-template-rows: 1fr 5fr;
`;

export default function Home() {
    return (
      <Wrapper>
        <PostTweetForm />
        <TimeLine />
      </Wrapper>
    );
}