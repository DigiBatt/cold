
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class ThermodynamicGrueneisenParameter(ISQDimensionlessQuantity, CondensedMatterPhysicsQuantity):
    """
    Class representing the `ThermodynamicGrueneisenParameter` entity, which inherits from:
    - ISQDimensionlessQuantity, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ff4dfc0f_6d79_41e1_9e32_68801bdea085'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermodynamicGrueneisenParameter'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermodynamicGrueneisenParameter(
    
    class_iri='https://w3id.org/emmo#EMMO_ff4dfc0f_6d79_41e1_9e32_68801bdea085',
    
    class_name='ThermodynamicGrueneisenParameter',
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ff4dfc0f_6d79_41e1_9e32_68801bdea085',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermodynamicGrueneisenParameter',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    