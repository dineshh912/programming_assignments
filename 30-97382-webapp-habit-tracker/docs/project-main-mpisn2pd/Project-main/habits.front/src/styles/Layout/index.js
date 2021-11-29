import React from 'react';
import { Container, Content } from './styles';

function Layout(){
  return(
    <Container>
      <div>Header</div>
      <Content>
        <div>Sidebar</div>
      </Content>
    </Container>
  );
}

export default React.memo(Layout);