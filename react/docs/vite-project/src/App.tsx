// import LinkedButton from "./myButton"

// function App() {
//   return (
//     <div>
//       <h1> Welcome to my world </h1>
//       <LinkedButton></LinkedButton>
//     </div>
//   )

// }

// export default App

function Profile() {
  return <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Ketherine Johnson" />;
}

function App() {
  return <section>
    <h1> "Amazing scientist"</h1>
    <Profile />
    <Profile />
    <Profile />
  </section>
}

export default App
