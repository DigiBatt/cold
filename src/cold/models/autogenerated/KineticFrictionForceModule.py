
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ForceModule import Force



from .MechanicalQuantityModule import MechanicalQuantity







class KineticFrictionForce(Force, MechanicalQuantity):
    """
    Class representing the `KineticFrictionForce` entity, which inherits from:
    - Force, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fe3eb868_8745_4fea_8370_4313d0531c18'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KineticFrictionForce'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KineticFrictionForce(
    
    class_iri='https://w3id.org/emmo#EMMO_fe3eb868_8745_4fea_8370_4313d0531c18',
    
    class_name='KineticFrictionForce',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fe3eb868_8745_4fea_8370_4313d0531c18',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KineticFrictionForce',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    