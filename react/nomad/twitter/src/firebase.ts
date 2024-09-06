import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDUjJdBVqVG5jOmsq-gt2s2QFZ62gZF-7k",
  authDomain: "twitter-clone-bbc50.firebaseapp.com",
  projectId: "twitter-clone-bbc50",
  storageBucket: "twitter-clone-bbc50.appspot.com",
  messagingSenderId: "296978065622",
  appId: "1:296978065622:web:d6d5add38aaafbe207c177",
  measurementId: "G-F090WQPHH6"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
