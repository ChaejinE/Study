import { useEffect, useState } from "react";
import styled from "styled-components";
import { collection, getDocs, orderBy, query } from "firebase/firestore";
import { db } from "../src/firebase";
import Tweet from './tweet';

export interface ITweet {
  id: string;
  photo?: string;
  tweet: string;
  userId: string;
  username: string;
  createdAt: number;
}

const Wrapper = styled.div``;

export default function TimeLine() {
  const [tweets, setTweets] = useState<ITweet[]>([]);
  const fetcTweets = async () => {
    const tweetsQuery = query(collection(db, "tweets"), orderBy("createdAt", "desc"));
    const snapShot = await getDocs(tweetsQuery);
    const tweets = snapShot.docs.map((doc) => {
      const {tweet, createdAt, userId, username, photo} = doc.data();
      return {
        tweet, createdAt, userId, username, photo, id: doc.id
      }
    });
    console.log(JSON.stringify(tweets));
    setTweets(tweets);
  }

  useEffect(() => {
    fetcTweets();
  }, [])
  return (
    <Wrapper>
      {tweets.map((tweet) => <Tweet key={tweet.id} {...tweet} />)}
    </Wrapper>
  );
}
