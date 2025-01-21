
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity



from .RatioQuantityModule import RatioQuantity







class RelativeMassFractionOfVapour(ThermodynamicalQuantity, RatioQuantity):
    """
    Class representing the `RelativeMassFractionOfVapour` entity, which inherits from:
    - ThermodynamicalQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a45dc074_c5ed_4aad_a4e7_141a02fe1d73'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RelativeMassFractionOfVapour'`
        - **Alias**: `class_name`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RelativeMassFractionOfVapour(
    
    class_iri='https://w3id.org/emmo#EMMO_a45dc074_c5ed_4aad_a4e7_141a02fe1d73',
    
    class_name='RelativeMassFractionOfVapour',
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a45dc074_c5ed_4aad_a4e7_141a02fe1d73',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RelativeMassFractionOfVapour',
        alias="class_name"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    