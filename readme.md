# Litepi, the Mindnight Bot

## The Game

In Mindnight there are two roles, the **Agents** and the **Hackers**.
The **Agents** have to figure out who the **Hackers** are and exclude them from the game.
The **Hackers** have to sabotage the **Agents** and make them lose the game.

### Gameplay

The game has up to half the players in **Nodes**.
Each **Node** has to be hacked, by the **Hackers**, or secured, by the **Agents**.
But first a *proposition* has to be made by the players.
Here, N/2+1 players have to be selected to participate in the **Node**.
After a *proposition* is made, the players have to vote to accept or reject the *proposition*.
If the *proposition* is denied, the next player in line has to make a *proposition*.
A **Node** can only have 4 denied *propositions* before it is automatically accepted.
If the *proposition* is accepted, the participants have to vote to hack or secure the **Node**.
**Agents** can only secure **Nodes** and **Hackers** may choose to hack or secure **Nodes**.
If the majority of **Nodes** are hacked, the **Hackers** win.
If the majority of **Nodes** are secured, the **Agents** win.

### Roles

#### Agent

The **Agents** have to find the **Hackers** and exclude them from propostions.
The **Agents** can only secure **Nodes**.
The **Agents** win if the majority of **Nodes** are secured.

#### Hacker

The **Hackers** have to sabotage the **Agents** and make them lose the game.
The **Hackers** can hack or secure **Nodes**.
The **Hackers** win if the majority of **Nodes** are hacked.

## The Bot

The bot is a Discord bot that can be used to play Mindnight.
It is written in Python and uses the [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) library.

### Commands

The bot has a few commands that can be used to play the game.
The commands are listed below.

#### `/help`

The `/help` command lists all the commands that the bot has.

#### `/start`

The `/start` command starts a game of Mindnight.
The command can only be used by the server owner.
The command creates a new channel called `mindnight-x` where x is the game number.
The command also creates a new role called `Mindnight x` where x is the game number.

#### `/join x`

The `/join x` command joins the game with the game number x.
If the player is already in a game, the command will not work.
The command can only be used by members of the server.
The command adds the member to the `Mindnight x` role.
If x is not a valid game number, or 0, a random game is selected.

#### `/leave`

The `/leave` command leaves the game that the member is in.
The command can only be used by members of the server.
The command removes the member from the `Mindnight x` role.

#### `/propose x`

The `/propose x` command proposes a **Node** where x is a list of players.
The command can only be used by players in a game.
The command can only be used by the player that is in turn.

#### `/accept`

The `/accept` command accepts the current *proposal*.
The command can only be used by players in a game.

#### `/reject`

The `/reject` command rejects the current *proposal*.
The command can only be used by players in a game.

#### `/hack`

The `/hack` command hacks the current **Node**.
The command can only be used by players in a game.
The command can only be used by **Hackers**.

#### `/secure`

The `/secure` command secures the current **Node**.
The command can only be used by players in a game.

#### `/end`

The `/end` command ends the game that the member is in.
The command can only be used by the server owner.
The command removes the `Mindnight x` role.
The command deletes the `mindnight-x` channel.

### Permissions

The bot needs the following permissions to work properly.

- `Send Messages`
- `Embed Links`
- `Read Message History`
- `Add Reactions`
- `Manage Channels`
- `Manage Roles`

### Installation

The bot can be installed by cloning the repository and installing the requirements.
The bot can be run by running the `bot.py` file in the `bot` directory.

