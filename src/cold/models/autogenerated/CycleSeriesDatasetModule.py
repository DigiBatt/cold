
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatrixModule import Matrix



from .WholeModule import Whole



from .ObjectModule import Object





from .ConstituentModule import Constituent





class CycleSeriesDataset(Matrix, Whole, Object):
    """
    Class representing the `CycleSeriesDataset` entity, which inherits from:
    - Matrix, Whole, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2f6f1a6_4dee_4c5e_9a69_32b9fe990d2f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CycleSeriesDataset'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CycleSeriesDataset(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2f6f1a6_4dee_4c5e_9a69_32b9fe990d2f',
    
    class_name='CycleSeriesDataset',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2f6f1a6_4dee_4c5e_9a69_32b9fe990d2f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CycleSeriesDataset',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    