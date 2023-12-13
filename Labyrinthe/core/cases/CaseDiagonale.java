package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseDiagonale extends Case
{
    public CaseDiagonale()
    {
        super("diagonale", new Position(), 0, null, false, false);
    }

    public CaseDiagonale(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("Diagonale", position, rotation, objet, depart, fixe);
    }

    public CaseDiagonale(CaseDiagonale c)
    {
        super(c);
    }

    public CaseDiagonale newInstance()
    {
        CaseDiagonale newCase = new CaseDiagonale(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
        String contenu = "";
        if (this.rotation == 0 || this.rotation == 180)
            contenu = "/";
        else if (this.rotation == 90 || this.rotation == 270)
            contenu = "\\";
        
        return contenu;
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        if (this.rotation == 0 || rotation == 180) // /
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() + 1)); // bas gauche
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() - 1)); // haut droit
        }
        else if (this.rotation == 90 || this.rotation == 270) // \
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() - 1)); // haut gauche
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() + 1)); // bas droit
        }

        return deplacementpossible;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseDiagonale == false)
            return false;
        else
        {
            CaseDiagonale caseDiagonale = (CaseDiagonale) o;
            return this.toString().equals(caseDiagonale.toString());
        }
    }
}