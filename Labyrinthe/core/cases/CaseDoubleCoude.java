package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseDoubleCoude extends Case
{
    public CaseDoubleCoude()
    {
        super("double coude", new Position(), 0, null, false, false);
    }

    public CaseDoubleCoude(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("double coude", position, rotation, objet, depart, fixe);
    }

    public CaseDoubleCoude(CaseDoubleCoude c)
    {
        super(c);
    }

    public CaseDoubleCoude newInstance()
    {
        CaseDoubleCoude newCase = new CaseDoubleCoude(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
        String contenu = "";
        if (this.rotation == 0 || this.rotation == 180)
            contenu = "?";
        else if (this.rotation == 90 || this.rotation == 270)
            contenu = "¿";
        
        return contenu;
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        return null;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseDoubleCoude == false)
            return false;
        else
        {
            CaseDoubleCoude caseDoubleCoude = (CaseDoubleCoude) o;
            return this.toString().equals(caseDoubleCoude.toString());
        }
    }
}