import { useEffect, useState } from "react";
import styled from "styled-components";
import { collection, getDocs, limit, onSnapshot, orderBy, query } from "firebase/firestore";
import { db } from "../src/firebase";
import Tweet from './tweet';
import { Unsubscribe } from "firebase/auth";

export interface ITweet {
  id: string;
  photo?: string;
  tweet: string;
  userId: string;
  username: string;
  createdAt: number;
}

const Wrapper = styled.div`
  display: flex;
  gap: 10px;
  flex-direction: column;
`;

export default function TimeLine() {
  const [tweets, setTweets] = useState<ITweet[]>([]);

  const maxTweetLimit = 25;

  useEffect(() => {
    let unsubscribe :Unsubscribe | null = null;
    const fetcTweets = async () => {
      const tweetsQuery = query(
        collection(db, "tweets"), 
        orderBy("createdAt", "desc"),
        limit(maxTweetLimit)
      );
      
      // change to real-time
      // const snapShot = await getDocs(tweetsQuery);
      // const tweets = snapShot.docs.map((doc) => {
      //   const {tweet, createdAt, userId, username, photo} = doc.data();
      //   return {
      //     tweet, createdAt, userId, username, photo, id: doc.id
      //   }
      // });
      unsubscribe = await onSnapshot(tweetsQuery, (snapshot) => {
        const tweets = snapshot.docs.map((doc) => {
          const {tweet, createdAt, userId, username, photo} = doc.data();
          return {
            tweet, createdAt, userId, username, photo, id: doc.id
          }
        });
        setTweets(tweets);
      })
    }

    fetcTweets()

    return () => { unsubscribe && unsubscribe() };
  }, [])
  return (
    <Wrapper>
      {tweets.map((tweet) => <Tweet key={tweet.id} {...tweet} />)}
    </Wrapper>
  );
}
