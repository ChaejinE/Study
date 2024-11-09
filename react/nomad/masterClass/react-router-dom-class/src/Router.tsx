import { createBrowserRouter } from "react-router-dom";
import Root from "./Root"
import About from "./screens/About";
import Home from "./screens/Home";
import NotFound from "./screens/NotFound";
import ErrorComponent from "./components/ErrorComponent";
import User from "./screens/users/User";
import Followers from "./screens/users/Followers";

// This makes the structure of routes could be list
const router = createBrowserRouter([
   {
      // Container of all routes
      path: "/",
      element: <Root />,
      children: [
        {
          path: "",
          element: <Home />,
          errorElement: <ErrorComponent /> // for being protected from some problems
        },
        {
          path: "about",
          element: <About />
        },
        {
          path: "users/:userId", // for dynamic param
          element: <User />,
          children: [
            {
              path: "followers",
              element: <Followers />
            }
          ]
        }
      ],
      errorElement: <NotFound />
   }
])

export default router;
