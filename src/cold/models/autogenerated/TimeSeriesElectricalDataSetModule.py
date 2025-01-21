
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeSeriesDataSetModule import TimeSeriesDataSet





from .ConstituentModule import Constituent





class TimeSeriesElectricalDataSet(TimeSeriesDataSet):
    """
    Class representing the `TimeSeriesElectricalDataSet` entity, which inherits from:
    - TimeSeriesDataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31e8052d_bede_43c6_8b41_d51bb24c9489'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TimeSeriesElectricalDataSet'`
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
    obj = TimeSeriesElectricalDataSet(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31e8052d_bede_43c6_8b41_d51bb24c9489',
    
    class_name='TimeSeriesElectricalDataSet',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31e8052d_bede_43c6_8b41_d51bb24c9489',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TimeSeriesElectricalDataSet',
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
    
    

    

    