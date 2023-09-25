import { useState } from 'react';
import './App.css';

function App() {
  const blogTitle = "React Blog";
  let [titles, setTitles] = useState(["남자 코트 추천", "여자 코트 추천", "노인 코트 추천"]); // destructing
  let [selectedIdx, setSelectedIdx] = useState(0);
  let [good, setGood] = useState([0, 0, 0]);
  let [modal, setModal] = useState(false);
  let publishTitle = "";

  return (
    <div className="App">
      <div className="black-nav">
        <h4>{blogTitle}</h4>
      </div>

      {
        titles.map((data, idx) => {
          return (
            <div className="list" key={idx}>
              <h4 onClick={() => { 
                  setSelectedIdx(idx);
                  setModal(modal^true);
                }}>{ data } 
                <span onClick={(e) => {
                  e.stopPropagation();
                  let copy = [...good];
                  copy[idx]++;
                  setGood(copy);
                }}>👍 좋아요</span> {good[idx]}
                <button style={{marginLeft: "20px"}} onClick={(e) => {
                  let copy = titles.filter((elem) => { return elem != data})
                  e.stopPropagation();
                  setTitles(copy);
                }}>삭제</button>
              </h4>
              <p>2월 17일</p>
            </div>
          )
        })
      }

      <div>
        <input onChange={(e) => {publishTitle = e.target.value}} type="text" />
        <button onClick={() => {
          let copy = [...titles];
          copy.push(publishTitle);
          setTitles(copy);
          copy = [...good];
          copy.push(0);
          setGood(copy);
        }}>Publish</button>
      </div>

      {
        modal ? <Modal title={titles[selectedIdx]}/> : null
      }

      
    </div>
  );
}

function Modal(props){
  return (
    <>
      <div className="modal">
        <h4>{props.title}</h4>
        <p>날짜</p>
        <p>상세내용</p>
        <button onClick={() => {
        }}>글수정</button>
      </div>
    </>
  )
}

export default App;
