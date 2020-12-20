Module code.planet_system_creation
==================================

Classes
-------

`Massiveobject(name, mass, x, v, F)`
:   Representation of a physical object.
    
    This class should represent the sun or a planet or a rocket.
    It has 4 attributes, name, mass, position x, starting velocity v.
    The last 3 parameters are necessary to solve the differential equation
    which governs the motion of the planets
    
    Set values for name, mass, place, velocity and force.

    ### Descendants

    * code.planet_system_creation.Planet
    * code.planet_system_creation.Rocket

`Planet(name, mass, x, v, F, radius, period)`
:   Representation of a planet.
    
    Inherit all properties of the Massiveobject class.
    Then add the properties radius and orbital period.
    
    Set values for name, mass, place, velocity and force.

    ### Ancestors (in MRO)

    * code.planet_system_creation.Massiveobject

`Rocket(name, mass, x, v, F, length, passengers)`
:   Representation of a rocket.
    
    Inherit all properties of the Massiveobject class.
    Then add the properties length and number of passengers.
    
    Set values for name, mass, place, velocity and force.

    ### Ancestors (in MRO)

    * code.planet_system_creation.Massiveobject