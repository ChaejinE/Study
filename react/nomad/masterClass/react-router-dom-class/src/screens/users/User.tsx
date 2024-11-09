import { Link, Outlet, useParams } from "react-router-dom";
import { users } from "../../db";

function User() {
  const {userId} = useParams();
  // Outlet is used if it has some child
  // U should write relative path in the "to" of the Link
  return (
    <div>
      <h1>User with it {userId} is named: {users[Number(userId) - 1].name}</h1>
      <hr />
      <Link to="followers">See followers</Link>
      <Outlet />
    </div>
  );
}

export default User;
