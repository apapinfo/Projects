package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CasePlus extends Case 
{
    public CasePlus()
    {
        super("plus", new Position(), 0, null, false, false);
    }

    public CasePlus(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("Plus", position, rotation, objet, depart, fixe);
    }

    public CasePlus(CasePlus c)
    {
        super(c);
    }

    public CasePlus newInstance()
    {
        CasePlus newCase = new CasePlus(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
            return "+";
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        // -
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite

        // |
        deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
        deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas

        return deplacementpossible;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CasePlus == false)
            return false;
        else
        {
            CasePlus casePlus = (CasePlus) o;
            return this.toString().equals(casePlus.toString());
        }
    }
}