import { Link } from "react-router-dom";

function Header() {
    // For using Link, u should put it  in the BrowserRouter
  return ( 
    <header>
      <ul>
        <li>
          <Link to={"/"}>Home</Link>
        </li>
        <li>
          <Link to={"/about"}>About</Link>
        </li>
      </ul> 
    </header>
  );
}

export default Header;
