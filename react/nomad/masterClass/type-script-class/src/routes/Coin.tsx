import { useParams } from "react-router-dom";

interface CoindParams {
  coinId: string;
}

function Coin() {
  const { coinId } = useParams<CoindParams>();
  return <h1>Coin : {coinId}</h1>;
};

export default Coin;
