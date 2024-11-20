import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { fetchCoins } from "../api";
import { Helmet } from "react-helmet";

const Container = styled.div`
  padding: 0px 20px;
  max-width: 480px;
  margin: 0 auto;
`;

const Header = styled.header`
  height: 10vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const CoinsList = styled.ul``;

const Coin = styled.li`
  background-color: white;
  color: ${props => props.theme.textColor};
  margin-bottom: 10px;
  border-radius: 15px;
  a {
    display: flex;
    padding: 20px;
    transition: color 0.2s ease-in;
    align-items: center;
  }
  &:hover {
    a {
      color: ${props => props.theme.accentColor};
    }
  }
`;

const Title = styled.h1`
  font-size: 48px;
  color: ${props => props.theme.accentColor};
`;

const Loader = styled.span`
  text-align: center;
  display: block;
`;

const Img = styled.img`
  width: 35px;
  height: 35px;
  margin-right: 10px;
`;

interface ICoin {
  id: string;
  name: string;
  symbol: string;
  rank: number;
  is_new: boolean;
  is_active: boolean;
  type: string;
}

interface ICoinsProps {
  toggleDark: () => void;
  isDark: boolean;
}

function Coins({toggleDark}: ICoinsProps) {
  // 1. unique identifier 2. fetch function
  const { isLoading, data } = useQuery<ICoin[]>("allCoins", fetchCoins)
  // because react query keeps data as  a cache, we don't need to see Loading when we go to back
  // It's very awsome !

  return (
    <Container>
      <Helmet>
        <title>코인</title>
      </Helmet>
      <Header>
        <Title>코인</Title>  
        <button onClick={toggleDark}>Toggle Mode</button>
      </Header>
      {isLoading  ? 
        <Loader>Loading...</Loader> : 
        <CoinsList>
          {data?.slice(0, 100).map((coin) => {
            return (
              <Coin key={coin.id}>
                <Link to={{
                  pathname: `/${coin.id}`,
                  state: { name: coin.name }
                }}>
                  <Img src={`https://cryptocurrencyliveprices.com/img/${coin.id}.png`} />
                  {coin.name} &rarr;
                </Link>
              </Coin>
            );
          })}
        </CoinsList>
      }
    </Container>
  );
};

export default Coins;
