
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntensiveModule import Intensive



from .ChemicalCompositionQuantityModule import ChemicalCompositionQuantity



from .ConcentrationModule import Concentration



from .ISQDerivedQuantityModule import ISQDerivedQuantity





from .MeasurementUnitModule import MeasurementUnit





class AmountConcentration(Intensive, ChemicalCompositionQuantity, Concentration, ISQDerivedQuantity):
    """
    Class representing the `AmountConcentration` entity, which inherits from:
    - Intensive, ChemicalCompositionQuantity, Concentration, ISQDerivedQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d5be1faf_0c56_4f5a_9b78_581e6dee949f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmountConcentration'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmountConcentration(
    
    class_iri='https://w3id.org/emmo#EMMO_d5be1faf_0c56_4f5a_9b78_581e6dee949f',
    
    class_name='AmountConcentration',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d5be1faf_0c56_4f5a_9b78_581e6dee949f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmountConcentration',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
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
    
    

    

    