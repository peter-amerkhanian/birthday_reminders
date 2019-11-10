import React from 'react';
import { List, Header } from "semantic-ui-react";

export const Names = ({ names }) => {
    return (
        <List>
            {names.map(name => {
                return (
                    <List.Item key={name.name}>
                        <Header>{name.name}
                        </Header>
                    </List.Item>
                )
            })}
        </List>
    )
};