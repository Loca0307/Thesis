
    public boolean noBlackArrowsRemain()
    {
        for (int r=0; r<NUM_ROWS; r++)
            for (int c=0; c<NUM_COLS; c++)
                if (myGrid[r][c].getMyColor() == Color.BLACK)
                    return false;
        return true;
    }

    public ArrowCell targetOfArrowCell(ArrowCell cell)
    {
        switch (cell.getDirection())
        {
            case ArrowCell.RIGHT:
                if (cell.getMyCol() == NUM_COLS-1)
                    return null;
                return myGrid[cell.getMyRow()][cell.getMyCol()+1];
            case ArrowCell.LEFT:
                if (cell.getMyCol() == 0)
                    return null;
                return myGrid[cell.getMyRow()][cell.getMyCol()-1];
            case ArrowCell.DOWN:
                if (cell.getMyRow() == NUM_ROWS-1)
                    return null;
                return myGrid[cell.getMyRow()+1][cell.getMyCol()];
            case ArrowCell.UP:
                if (cell.getMyRow() == 0)
                    return null;
                return myGrid[cell.getMyRow()-1][cell.getMyCol()];

            default:
                return null;
        }

    }

    public void setColorForPath(Color c, ArrayList<ArrowCell> path)
    {
        for (ArrowCell cell:path)
        {
            cell.setMyColor(c);
        }
        repaint();
    }

    public void colorPathStartingAt(int r, int c)
    {
        ArrowCell startCell = myGrid[r][c];
        if (startCell.getMyColor() != Color.BLACK)
            return;
        ArrayList<ArrowCell> path = new ArrayList<>();
        path.add(startCell);
        while(true)
        {
            ArrowCell nextCell = targetOfArrowCell(path.get(path.size()-1));
            if (nextCell == null || path.contains(nextCell))
            {
                if (nextCell != null)
                    path.add(nextCell);
                setColorForPath(new Color((int)(Math.random()*128)+64,
                                (int)(Math.random()*128)+64,
                                (int)(Math.random()*128)+64),
                        path);
                return;
            }
            if (nextCell.getMyColor() != Color.BLACK)
            {
                setColorForPath(nextCell.getMyColor(), path);
                return;
            }
            path.add(nextCell);
        }
    }

    public void execute()
    {
        for (int cellNum = 0; cellNum<NUM_ROWS*NUM_COLS; cellNum++)
            colorPathStartingAt(cellNum/NUM_COLS, cellNum%NUM_COLS);

    }