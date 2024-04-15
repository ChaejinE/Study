import Card from "../utils/card";
import axios from "axios";

function Home(props) {

    return (
        <>
            <div className="main-bg" style={{backgroundImage: `url(${process.env.PUBLIC_URL}/img/bg.png)`}}></div>

            <div className="container">
                <div className="row">
                {
                    props.shoes.map((elem, idx) => {
                    return (
                        <Card title={elem.title} content={elem.content} idx={idx} key={idx}/>
                    )
                    })
                }
                </div>

                <button onClick={() => {
                    axios.get("https://codingapple1.github.io/shop/data2.json")
                        .then((res) => {
                            let newData = res.data;
                            let newShoes = [...props.shoes, ...newData];
                            props.setShoes(newShoes);
                        })
                        .catch((err) => {
                            console.log(err);
                        })
                }}>
                    버튼
                </button>
            </div>
        </>
    )
}

export default Home;
