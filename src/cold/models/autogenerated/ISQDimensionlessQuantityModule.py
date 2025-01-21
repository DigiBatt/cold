
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity





from .MetrologicalReferenceModule import MetrologicalReference





class ISQDimensionlessQuantity(ISQDerivedQuantity):
    """
    Class representing the `ISQDimensionlessQuantity` entity, which inherits from:
    - ISQDerivedQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a66427d1_9932_4363_9ec5_7d91f2bfda1e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ISQDimensionlessQuantity'`
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
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ISQDimensionlessQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_a66427d1_9932_4363_9ec5_7d91f2bfda1e',
    
    class_name='ISQDimensionlessQuantity',
    
    iupacReference="example_value",
    
    hasMetrologicalReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a66427d1_9932_4363_9ec5_7d91f2bfda1e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ISQDimensionlessQuantity',
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
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasMetrologicalReference", pre=True, always=True)
    def validate_hasMetrologicalReference(cls, value):
        if value is not None and not isinstance(value, MetrologicalReference):
            raise ValueError(f"Field 'hasMetrologicalReference' must be an instance of 'MetrologicalReference' or its subclass.")
        return value
    
    

    

    