import Box from '@mui/material/Box';
import MContainer from '@mui/material/Container';
import { styled } from '@mui/material/styles';

export const Container = styled(MContainer)`
  padding: 0;

  ${(props) => props.theme.breakpoints.up('lg')} {
    color: white;
    max-width: 1300px;
    height: 100vh;
  }
  ${(props) => props.theme.breakpoints.down('lg')} {
    height: 100%;
  }
`;

export const Content = styled(Box)`
  width: 100%;

  ${(props) => props.theme.breakpoints.up('lg')} {
    display: inline-grid;
    grid-template-columns: 20% 80%;
  }
  ${(props) => props.theme.breakpoints.down('lg')} {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
`;
