import { Outlet } from "react-router-dom"
import Header from "./components/Header"

function Root() {

  return (
    // The Outlet replaces  the path to Route's
    // It seems that it's really similar with placeholder 
    // The Oulet context makes children know about the context
    // The children could use the context using a useOuletContext hook
    <>
      <Header />
      <Outlet context={{ darkMode: true }}/>
    </>
  )
}

export default Root
