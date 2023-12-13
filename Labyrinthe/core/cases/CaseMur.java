package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseMur extends Case
{
    public CaseMur()
    {
        super("mur", new Position(), 0, null, false, false);
    }

    public CaseMur(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("Mur", position, rotation, objet, depart, fixe);
    }

    public CaseMur(CaseMur c)
    {
        super(c);
    }

    public CaseMur newInstance()
    {
        CaseMur newCase = new CaseMur(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
        return "■";
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        return null;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseMur == false)
            return false;
        else
        {
            CaseMur caseMur = (CaseMur) o;
            return this.toString().equals(caseMur.toString());
        }
    }
}