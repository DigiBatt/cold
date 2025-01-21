
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalQuantityModule import PhysicalQuantity







class PhysicalConstant(PhysicalQuantity):
    """
    Class representing the `PhysicalConstant` entity, which inherits from:
    - PhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b953f2b1_c8d1_4dd9_b630_d3ef6580c2bb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalConstant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_b953f2b1_c8d1_4dd9_b630_d3ef6580c2bb',
    
    class_name='PhysicalConstant',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b953f2b1_c8d1_4dd9_b630_d3ef6580c2bb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalConstant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    