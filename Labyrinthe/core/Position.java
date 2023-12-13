package labyrinthe.core;

public class Position 
{
    private int longueur, hauteur;
    
    public Position()
    {
        this.longueur = this.hauteur = 0;
    }

    public Position(int longueur, int hauteur)
    {
        this.longueur = longueur;
        this.hauteur = hauteur;
    }

    // set/get longueur
    public void setLongueur(int longueur)
    {
        this.longueur = longueur;
    }

    public int getLongueur()
    {
        return this.longueur;
    }

    // set/get hauteur

    public void setHauteur(int hauteur)
    {
        this.hauteur = hauteur;
    }

    public int getHauteur()
    {
        return this.hauteur;
    }

    @Override
    public String toString()
    {
        return "(" + this.longueur + "," + this.hauteur + ")";
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof Position == false)
            return false;
        else
        {
        Position position = (Position) o;
        return (this.toString().equals(position.toString()));
        }
    }
}