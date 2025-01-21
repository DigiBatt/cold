
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicConstructModule import SymbolicConstruct



from .MetrologicalModule import Metrological



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation





from .NumericalModule import Numerical



from .MetrologicalReferenceModule import MetrologicalReference





class QuantityValue(SymbolicConstruct, Metrological, SpatioTemporalTessellation):
    """
    Class representing the `QuantityValue` entity, which inherits from:
    - SymbolicConstruct, Metrological, SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f658c301_ce93_46cf_9639_4eace2c5d1d5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'QuantityValue'`
        - **Alias**: `class_name`
    
    - `hasNumericalPart` (`Optional[Numerical]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalPart`
    
    - `hasReferencePart` (`Optional[MetrologicalReference]`): 
        - **Default Value**: `None`
        - **Alias**: `hasReferencePart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = QuantityValue(
    
    class_iri='https://w3id.org/emmo#EMMO_f658c301_ce93_46cf_9639_4eace2c5d1d5',
    
    class_name='QuantityValue',
    
    hasNumericalPart="example_value",
    
    hasReferencePart="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f658c301_ce93_46cf_9639_4eace2c5d1d5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'QuantityValue',
        alias="class_name"
    )
    
    hasNumericalPart: Optional[Numerical] = Field(
        None,
        alias="hasNumericalPart"
    )
    
    hasReferencePart: Optional[MetrologicalReference] = Field(
        None,
        alias="hasReferencePart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    @validator("hasNumericalPart", pre=True, always=True)
    def validate_hasNumericalPart(cls, value):
        if value is not None and not isinstance(value, Numerical):
            raise ValueError(f"Field 'hasNumericalPart' must be an instance of 'Numerical' or its subclass.")
        return value
    
    @validator("hasReferencePart", pre=True, always=True)
    def validate_hasReferencePart(cls, value):
        if value is not None and not isinstance(value, MetrologicalReference):
            raise ValueError(f"Field 'hasReferencePart' must be an instance of 'MetrologicalReference' or its subclass.")
        return value
    
    

    

    