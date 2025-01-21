
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity





from .MeasurementUnitModule import MeasurementUnit





class QuarterTransitionTimePotential(ElectrochemicalQuantity):
    """
    Class representing the `QuarterTransitionTimePotential` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2705525b_7512_48bf_825b_f2d0409bede4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'QuarterTransitionTimePotential'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = QuarterTransitionTimePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2705525b_7512_48bf_825b_f2d0409bede4',
    
    class_name='QuarterTransitionTimePotential',
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2705525b_7512_48bf_825b_f2d0409bede4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'QuarterTransitionTimePotential',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasMeasurementUnit: Optional[MeasurementUnit] = Field(
        None,
        alias="hasMeasurementUnit"
    )
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    