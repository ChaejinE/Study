import './App.css';
import { Nav, Navbar, Container} from 'react-bootstrap';
import { Routes, Route, useNavigate, Outlet} from "react-router-dom";
import data from "./data"
import { useState } from "react";
import Detail from './pages/detail';
import Home from './pages/home';

function App() {
  let [shoes, setShoes] = useState(data);
  let navigate = useNavigate();

  return (
    <div className="App">
      <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand onClick={() => { navigate("/"); }
        }>Shoe Shop</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link onClick={(e) => { 
                navigate("/cart");
                e.stopPropagation(); 
              }
            }>Cart</Nav.Link>
          </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Routes>
        <Route path="/" element={<Home shoes={shoes} setShoes={setShoes}/>}></Route>
        <Route path="/detail/:id" element={<Detail shoes={shoes}/>}/>
        <Route path="/cart" element={<div>장바구니페이지임</div>}/>
        <Route path="*" element={<div>404 Not Found</div>}/>
      </Routes>
    </div>
  );
}

function About() {
  return (
    <div>
      <h4>회사정보</h4>
      <Outlet></Outlet>
    </div>
  )
}

export default App;
