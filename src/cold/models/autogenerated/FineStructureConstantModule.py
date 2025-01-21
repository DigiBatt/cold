
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuredConstantModule import MeasuredConstant





from .MetrologicalReferenceModule import MetrologicalReference





class FineStructureConstant(MeasuredConstant):
    """
    Class representing the `FineStructureConstant` entity, which inherits from:
    - MeasuredConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d7d2ca25_03e1_4099_9220_c1a58df13ad0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FineStructureConstant'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `hasMetrologicalReference` (`Optional[MetrologicalReference]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetrologicalReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FineStructureConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_d7d2ca25_03e1_4099_9220_c1a58df13ad0',
    
    class_name='FineStructureConstant',
    
    iupacReference="example_value",
    
    hasMetrologicalReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d7d2ca25_03e1_4099_9220_c1a58df13ad0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FineStructureConstant',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    hasMetrologicalReference: Optional[MetrologicalReference] = Field(
        None,
        alias="hasMetrologicalReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    @validator("hasMetrologicalReference", pre=True, always=True)
    def validate_hasMetrologicalReference(cls, value):
        if value is not None and not isinstance(value, MetrologicalReference):
            raise ValueError(f"Field 'hasMetrologicalReference' must be an instance of 'MetrologicalReference' or its subclass.")
        return value
    
    

    

    