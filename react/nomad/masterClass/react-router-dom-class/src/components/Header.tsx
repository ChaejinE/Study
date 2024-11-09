import { Link, useNavigate } from "react-router-dom";

function Header() {
  const navigate = useNavigate();
  const onAboutClick = () => {
    navigate("/about");
  };

  // For using Link, u should put it  in the BrowserRouter
  // Diff between Link and useNavigate : https://velog.io/@ahn-sujin/React-Link-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%99%80-useNavigate%EC%9D%98-%EC%B0%A8%EC%9D%B4
  return ( 
    <header>
      <ul>
        <li>
          <Link to={"/"}>Home</Link>
        </li>
        <li>
          <button onClick={onAboutClick}>About</button>
        </li>
      </ul> 
    </header>
  );
}

export default Header;
