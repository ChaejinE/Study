import { useState } from "react"

function LinkedButton() {
  const [ liked, setLiked ] = useState(false);
  if (liked) return "<div>you liked this</div>";

  return <button onClick={() => {setLiked(true)}}> 클릭 ! </button>

}

export default LinkedButton
