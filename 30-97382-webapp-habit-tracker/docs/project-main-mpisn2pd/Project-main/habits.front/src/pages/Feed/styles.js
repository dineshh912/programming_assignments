import styled from 'styled-components';

import Box from '@mui/material/Box';

export const Container = styled(Box)`
  && {
    ${(props) => props.theme.breakpoints.up('lg')} {
      display: inline-grid;
      grid-template-columns: 65% 35%;
      width: 100%;
      overflow: hidden;
    }
  }
`;