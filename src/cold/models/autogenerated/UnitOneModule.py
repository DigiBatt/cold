
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DimensionlessUnitModule import DimensionlessUnit







class UnitOne(DimensionlessUnit):
    """
    Class representing the `UnitOne` entity, which inherits from:
    - DimensionlessUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5ebd5e01_0ed3_49a2_a30d_cd05cbe72978'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UnitOne'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UnitOne(
    
    class_iri='https://w3id.org/emmo#EMMO_5ebd5e01_0ed3_49a2_a30d_cd05cbe72978',
    
    class_name='UnitOne',
    
    definition="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5ebd5e01_0ed3_49a2_a30d_cd05cbe72978',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UnitOne',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    