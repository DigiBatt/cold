
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoefficientOfFrictionModule import CoefficientOfFriction



from .MechanicalQuantityModule import MechanicalQuantity







class KineticFrictionFactor(CoefficientOfFriction, MechanicalQuantity):
    """
    Class representing the `KineticFrictionFactor` entity, which inherits from:
    - CoefficientOfFriction, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_89d04b65_5b11_4916_b606_0cf3f007fcd9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KineticFrictionFactor'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KineticFrictionFactor(
    
    class_iri='https://w3id.org/emmo#EMMO_89d04b65_5b11_4916_b606_0cf3f007fcd9',
    
    class_name='KineticFrictionFactor',
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_89d04b65_5b11_4916_b606_0cf3f007fcd9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KineticFrictionFactor',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    