function Card(props) {
    return (
        <div className="col-md-4">
        <img src={`https://codingapple1.github.io/shop/shoes${props.idx+1}.jpg`} width="80%" alt="" />
        <h4>{props.title}</h4>
        <p>{props.content}</p>
        </div>
    )
}

export default Card;
