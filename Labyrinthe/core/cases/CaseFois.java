package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseFois extends Case
{
    public CaseFois()
    {
        super("fois", new Position(), 0, null, false, false);
    }

    public CaseFois(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("Fois", position, rotation, objet, depart, fixe);
    }

    public CaseFois(CaseFois c)
    {
        super(c);
    }

    public CaseFois newInstance()
    {
        CaseFois newCase = new CaseFois(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
            return "x";
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();
        
        // /
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() + 1)); // bas gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() - 1)); // haut droit

        // \
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() - 1)); // haut gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() + 1)); // bas droit

        return deplacementpossible;
    }
    
    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseFois == false)
            return false;
        else
        {
            CaseFois caseFois = (CaseFois) o;
            return this.toString().equals(caseFois.toString());
        }
    }
}