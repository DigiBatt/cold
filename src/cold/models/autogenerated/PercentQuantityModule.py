
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity





from .MetrologicalReferenceModule import MetrologicalReference





class PercentQuantity(RatioQuantity):
    """
    Class representing the `PercentQuantity` entity, which inherits from:
    - RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cf386c1e_e62b_43ef_9b0e_e5e58935d63f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PercentQuantity'`
        - **Alias**: `class_name`
    
    - `hasMetrologicalReference` (`Optional[MetrologicalReference]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetrologicalReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PercentQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cf386c1e_e62b_43ef_9b0e_e5e58935d63f',
    
    class_name='PercentQuantity',
    
    hasMetrologicalReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cf386c1e_e62b_43ef_9b0e_e5e58935d63f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PercentQuantity',
        alias="class_name"
    )
    
    hasMetrologicalReference: Optional[MetrologicalReference] = Field(
        None,
        alias="hasMetrologicalReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasMetrologicalReference", pre=True, always=True)
    def validate_hasMetrologicalReference(cls, value):
        if value is not None and not isinstance(value, MetrologicalReference):
            raise ValueError(f"Field 'hasMetrologicalReference' must be an instance of 'MetrologicalReference' or its subclass.")
        return value
    
    

    

    