import Card from "../utils/card";

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
            </div>
        </>
    )
}

export default Home;
