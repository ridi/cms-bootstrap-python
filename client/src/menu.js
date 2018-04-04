import React from 'react';
import ReactDom from 'react-dom';
import { Menu } from '@ridi/cms-ui';

ReactDom.render(
  <Menu items={window.menuData} />,
  document.getElementById('menu'),
);
