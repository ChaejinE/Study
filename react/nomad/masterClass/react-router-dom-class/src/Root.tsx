import { Outlet } from "react-router-dom"
import Header from "./components/Header"

function Root() {

  return (
    // The Outlet replaces  the path to Route's
    // It seems that it's really similar with placeholder 
    <>
      <Header />
      <Outlet />
    </>
  )
}

export default Root
